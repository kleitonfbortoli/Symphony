import React from 'react'
import {Router, Switch, Route} from 'react-router'

import Login from '../pages/login'
import Home from '../pages/home'
import CadastroPessoa from '../pages/cadastro-pessoa'
import CadastroDisciplina from '../pages/cadastro-disciplina'
import NotFound from './NotFound'
import PrivateRout from './PrivateRout'

import {history} from './history'

const Routes = () => (
    <Router history={history}>
        <Switch>
            <Route component={Login} exact path="/login"/>
            <PrivateRout component={Home} exact path="/"/>
            <PrivateRout component={CadastroPessoa} exact path="/cadastro-pessoa"/>
            <PrivateRout component={CadastroDisciplina} exact path="/cadastro-disciplina"/>
            <PrivateRout component={NotFound}/>
        </Switch>
    </Router>
)

export default Routes