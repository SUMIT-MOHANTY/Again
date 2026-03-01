import axios from "axios";

const api = axios.create({
  baseURL: "/api/v1",
  timeout: 10000,
  headers: { "Content-Type": "application/json" }
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    const { response } = error;
    let errorMessage = "Network error. Please try again.";
    let errorDetails = {};

    if (response) {
      const data = response.data || {};
      errorMessage = data.message || errorMessage;
      errorDetails = data.details || {};
      
      if (response.status === 401) {
        errorMessage = "Please log in to continue";
      } else if (response.status === 403) {
        errorMessage = "You don't have permission to perform this action";
      } else if (response.status === 404) {
        errorMessage = "The requested resource was not found";
      } else if (response.status >= 500) {
        errorMessage = "Server error. Please try again later";
      }
    } else if (error.request) {
      errorMessage = "Unable to connect to server";
    }

    const apiError = new Error(errorMessage);
    apiError.status = response?.status;
    apiError.details = errorDetails;
    return Promise.reject(apiError);
  }
);

export default api;
