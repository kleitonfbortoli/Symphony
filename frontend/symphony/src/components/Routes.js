import React from 'react'
import {Route} from 'react-router'

import Login from '../pages/login'

import teste_page from '../pages/teste_page'
// import NotFound from './NotFound'
import { SidebarData } from './SidebarData.js'



const Routes = (parameters) => {
    return <>
        <Route component={Login} path="/login" />
        {parameters.permission.map((value) => SidebarData[value].route)}
        <Route component={teste_page} path="/teste"/>
        {/* <PrivateRout component={NotFound}/> */}
    </>
}

export default Routes