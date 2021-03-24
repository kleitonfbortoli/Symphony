import React from 'react'
import { BrowserRouter, Switch} from 'react-router-dom';
import Routes from '../components/Routes'
import NavBar from '../components/NavBar.js'

import './App.css';
import {history} from '../components/history'

const App = () => (
    <main className="App">
        <BrowserRouter history={history}>
            <NavBar />
            <Switch>
                <Routes />
            </Switch>
        </BrowserRouter>
    </main>
)

export default App
