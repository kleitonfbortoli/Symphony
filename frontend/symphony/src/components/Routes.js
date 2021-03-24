import React from 'react'
import {Redirect, Route} from 'react-router'

import Login from '../pages/login'
import Home from '../pages/home'
import CadastroPessoa from '../pages/cadastro-pessoa'
import CadastroSerie from '../pages/cadastro-serie'
import CadastroPeriodo from '../pages/cadastro-periodo-academico'
import CadastroDisciplina from '../pages/cadastro-disciplina'
import NotFound from './NotFound'
import PrivateRout from './PrivateRout'



const Routes = () => (
    <>
        <Route component={Login} path="/login"/>
        <PrivateRout component={Home} path="/" exact/>
        <PrivateRout component={CadastroPessoa} path="/cadastro-pessoa"/>
        <PrivateRout component={CadastroPeriodo} path="/cadastro-periodo-academico"/>
        <PrivateRout component={CadastroSerie} path="/cadastro-serie"/>
        <PrivateRout component={CadastroDisciplina} path="/cadastro-disciplina"/>
        {/* <PrivateRout component={NotFound}/> */}
    </>
)

export default Routes