import React from 'react'
import { Redirect, Route } from 'react-router'

const PrivateRout = props => {
    const isLoged = !! localStorage.getItem('user-token');

    return isLoged ? <Route {...props}/> : <Redirect to="/login"/>
}

export default PrivateRout