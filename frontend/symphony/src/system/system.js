import axios from 'axios'
import { BASIC_URL } from './constants'

export class System
{
    static post(method, parameters, callback)
    {
        let url = BASIC_URL + method;
        let token = localStorage.getItem('user-token');
        if (token === null)
        {
            token = " ";
        }
        
        // console.log(url);
        // console.log(parameters);

        parameters.token_access = token;
        axios.post(url, parameters)
            .then(resp => {
                const { data } = resp
                if (data.status === '200') {
                    callback(data.response);
                }
                else {
                    alert('algo errado')
                }
            })
            .catch(function (error)
            {
                alert('erro')
            });
    }

    static get(method, parameters, callback)
    {
        let token = localStorage.getItem('user-token');
        method = BASIC_URL + method;
        method = method + "?token=" + token;
        if (typeof(parameters) !== "undefined") {
            for(var key in parameters) {
                method = method + "&" + key + "=" + parameters[key];
            }
        }

        axios.get(method)
        .then((resp) => {
            const { data } = resp
            if (data.status === '200')
            {
                callback(data.response);
            }
        })
        .catch(function (error)
        {
            alert('erro')
        })
    }

    static logout() {
        localStorage.setItem('user-token','')
    }
}
