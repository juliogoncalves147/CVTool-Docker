# Use the official Node.js image from the Docker Hub
FROM node:16

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application code into the container
COPY . .

# Expose port 3000
EXPOSE 3000

# Command to run the frontend service
CMD ["npm", "start"]
