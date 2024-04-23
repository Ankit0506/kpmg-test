FROM node:alpine3.11
RUN mkdir -p /app
WORKDIR /app
RUN npm install
COPY  . /frontend/
RUN npm run build

# Expose $PORT on container.
EXPOSE 80
ENV NUXT_HOST=0.0.0.0

# Start the app
CMD [ "npm", "start" ]
