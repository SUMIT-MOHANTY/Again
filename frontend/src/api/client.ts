import axios from 'axios'
const api = axios.create({ baseURL: process.env.REACT_APP_API_URL })
api.interceptors.request.use(config => {
  if (config.params && config.params._noCache) {
    config.headers['X-Cache-Bypass'] = 'true'
    delete config.params._noCache
  }
  return config
})
export default api
