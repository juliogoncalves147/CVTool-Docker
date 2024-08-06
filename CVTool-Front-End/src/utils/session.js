import { v4 as uuidv4 } from 'uuid';

const SESSION_KEY = 'sessionId';

export const getSessionId = () => {
    let sessionId = localStorage.getItem(SESSION_KEY);
    if (!sessionId) {
        sessionId = uuidv4();
        localStorage.setItem(SESSION_KEY, sessionId);
    }
    return sessionId;
};
