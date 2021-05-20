import React from 'react'
import {Route} from 'react-router'

import Login from '../pages/login'

import teste_page from '../pages/teste_page'
import AuditoriaDetails from '../pages/auditoria-details'

import { SidebarData } from './SidebarData.js'



const Routes = (parameters) => {
    return <>
        <Route component={Login} path="/login" />
        {parameters.permission.map((value) => SidebarData[value].route)}
        <Route component={teste_page} path="/list-pessoa"/>
        <Route component={AuditoriaDetails} path="/auditoria-details"/>
        {/* <PrivateRout component={NotFound}/> */}
    </>
}

export default Routes