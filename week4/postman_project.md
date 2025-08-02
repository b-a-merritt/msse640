# Integration Testing with Postman (Part 1)

## Part I: APIs and Integration Testing

### Introduction  
Integration testing checks how components or services work together. Postman helps test API endpoints by sending requests and inspecting responses. This document outlines HTTP basics, APIs, CORS, and public API resources needed for integration testing.

### Basic Functionality of HTTP  

- **Client and Server:** Clients (like browsers or Postman) send requests to servers, which reply with responses.
- **Requests & Responses:** HTTP requests include methods (GET, POST, etc.), headers, and optional body content. Responses return status codes and data.
- **Headers vs. Body:** Headers carry metadata (e.g., auth tokens); body carries content like JSON or HTML.
- **Status Codes:** Codes like `200 (OK)`, `404 (Not Found)`, and `500 (Internal Server Error)` indicate request outcomes.
- **HTTP Verbs:** GET retrieves, POST creates, PUT updates, DELETE removes resources. Additional methods like PATCH are less common.
- **Stateless Protocol:** HTTP is stateless—each request is independent, requiring separate session mechanisms (e.g., cookies or tokens).

### Role of APIs in Modern Applications  

APIs define how systems communicate. They enable services to share functionality or data—like a mobile app using a cloud service for user login or weather data.

#### Open APIs  
Open (public) APIs are accessible to external developers. They encourage integration and innovation by exposing services and data with minimal setup.

#### Example – Google Maps API  
Apps like ride-sharing platforms use Google Maps APIs to show locations and directions without building their own map systems.

### Cross-Origin Resource Sharing (CORS)  

CORS allows web apps to request data from different origins. Browsers block cross-domain calls by default (same-origin policy), but CORS headers can permit them.

- `Access-Control-Allow-Origin` lets a server specify allowed origins.
- Some requests trigger a preflight `OPTIONS` check.
- CORS is browser-enforced; Postman isn't affected.

### Public API Resources  

A great source of APIs is the [Public APIs GitHub Repository](https://github.com/public-apis/public-apis), which lists hundreds of open APIs by category.

You can find APIs for:
- Weather (e.g., OpenWeatherMap)
- Code (e.g., GitHub API)
- News (e.g., News API)
- Maps (e.g., Google Maps)
- Social media (e.g., Twitter API)

Most return JSON data and are ideal for integration testing with Postman.

### Conclusion  

Postman allows testing of APIs efficiently.

## Part II: Postman Demo

![postman walkthrough](./assets/postman-walkthrough.mp4)