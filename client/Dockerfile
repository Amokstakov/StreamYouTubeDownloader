FROM node:12.16.1 as build 

WORKDIR /app

COPY package*.json ./

RUN npm ci

COPY . .

RUN npm run build

#production
FROM nginx:stable-alpine
COPY --from=build /app/build /usr/share/nginx/html

RUN rm /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

