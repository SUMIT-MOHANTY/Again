import api from './client'
import { useQuery } from '@tanstack/react-query'
export const fetchBook = (id: number) => api.get(`/books/${id}`).then(r => r.data)
export const useBook = (id: number) => useQuery(['book', id], () => fetchBook(id), { staleTime: 5 * 60 * 1000 })
