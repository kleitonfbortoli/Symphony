import React, { useEffect, useState } from 'react'
import { BrowserRouter, Switch} from 'react-router-dom';
import Routes from '../components/Routes'
import NavBar from '../components/NavBar.js'

import './App.css';
import {history} from '../components/history'
import { System } from '../system/system'
import { POST_GET_PERMISSION } from '../system/constants'


const App = () => {

    const [permiss, setPermissiom] = useState([])

    

    useEffect(() => {
        System.post(POST_GET_PERMISSION, {}, (data) => {
          setPermissiom(data)
        })
    }, [])

    return <main className="App">
        <BrowserRouter history={history}>
            <NavBar permission={ permiss}/>
            <Switch>
                <Routes permission={ permiss}/>
            </Switch>
        </BrowserRouter>
    </main>
}

export default App
