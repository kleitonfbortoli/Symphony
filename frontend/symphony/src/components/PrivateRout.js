import React from 'react'
import { Redirect, Route } from 'react-router'

const PrivateRout = props => {
    const isLoged = !! localStorage.getItem('user-mail');

    return isLoged ? <Route {...props}/> : <Redirect to="/login"/>
}

export default PrivateRout