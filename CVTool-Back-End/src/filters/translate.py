from deep_translator import GoogleTranslator
from .CommonsHelper import remove_invisible_characters
import queue
import threading

def callTranslate(item, source, target):
    try:
        return GoogleTranslator(source="auto", target=target).translate(item["valor"])
    except Exception as e:
        print(f"Translation error: {e}")
        return item

def worker(q, results, from_language, to_language, lock):
    while True:
        task = q.get()
        if task is None:
            break
        index, item = task
        if item.get("tipo") == 'element' and item.get("valor") not in [' ', '', None, 'None'] and item.get("section") != "":
            if item.get("reserved") == True:
                with lock:
                    results[index] = item
            else:
                translated_texto = callTranslate(item, from_language, to_language)
                if translated_texto is not None:
                    item["valor"] = translated_texto
                with lock:
                    results[index] = item
        else:
            with lock:
                results[index] = item
        q.task_done()
        with lock:
            print(f"Processed item {index + 1} out of {len(results)} remaining")

def translate(from_language, to_language, parsed_file):
    q = queue.Queue()
    results = [None] * len(parsed_file)  # Pre-allocate a list to hold results
    lock = threading.Lock()
    num_threads = 5
    threads = []

    for index, item in enumerate(parsed_file):
        q.put((index, item))

    for _ in range(num_threads):
        t = threading.Thread(target=worker, args=(q, results, from_language, to_language, lock))
        t.start()
        threads.append(t)

    q.join()

    for _ in range(num_threads):
        q.put(None)
    for t in threads:
        t.join()
        
    sorted_list = sorted(results, key=lambda x: int(x['id']))

    return sorted_list

def translateQuery(parsedData, from_language, to_language):
    translatedData = translate(from_language, to_language, parsedData)
    translatedData = remove_invisible_characters(translatedData)
    return translatedData