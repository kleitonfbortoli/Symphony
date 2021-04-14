import axios from 'axios'
import { BASIC_URL } from './constants'

export class System
{
    constructor() { }

    static post(method, parameters, callback)
    {
        var url = BASIC_URL + method;
        var token = localStorage.getItem('user-token');
        console.log(token);
        if (token == null)
        {
            token = " ";
        }

        parameters.token_access = token;

        var retorno = axios.post(url, parameters)
        .then(resp => {
            const { data } = resp
            console.log(data);
            if (data.status == '200')
            {
                callback(data.response);
            }
        })
        .catch(function (error)
        {
            alert('erro')
            console.log(error.error);
        });

        return retorno
    }

    static logout() {
        localStorage.setItem('user-token','')
    }
}
