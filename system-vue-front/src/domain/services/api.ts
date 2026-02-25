import axios from 'axios'
import { useRouter } from 'vue-router'

export const BASE_URL = 'http://localhost:8000/'

export const BASE_URL_API = BASE_URL + 'v1/'

export const api = axios.create({
  baseURL: BASE_URL_API,
  timeout: 10000
})

api.interceptors.request.use(function (config) {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

api.interceptors.response.use(function (response) {
  var data = response.data
  if(data?.code == 401){
    const router = useRouter()
    localStorage.removeItem('token')
    router.push('/login')
  }

  return response
}, function (error) {
  if (error.response.status === 401) {
    const router = useRouter()
    localStorage.removeItem('token')
    router.push('/login')
  }
  return Promise.reject(error)
})
