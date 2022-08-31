import {axios} from '../axios';
import {path} from '@/api/conf_api';

export const signIn = (payload) => {
   return axios.post('login ',payload)
   .then(({data}) => {
        return Promise.resolve(data)
   })
   .catch((err) => {
       return Promise.reject(err)
   })
}