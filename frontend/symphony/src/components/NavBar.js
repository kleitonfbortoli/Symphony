import React, { useEffect, useState } from 'react'
import * as FaIcons from 'react-icons/fa'
import * as AiIcons from 'react-icons/ai'
import { Link } from 'react-router-dom'
import { IconContext } from 'react-icons'

import { SidebarData } from './SidebarData.js'
import { BASIC_URL, GET_TEMPERATURE } from '../system/constants'

import '../styles/scss/navbar/navbar.scss'

import axios from 'axios'

function NavBar(parameters) {
    const [sidebar, setSidebar] = useState(false)

    const showSidebar = () => setSidebar(!sidebar)

    // const reloadTemperature = () => {
    //     axios.get(BASIC_URL + GET_TEMPERATURE)
    //         .then((data) => {
    //             let temp = data.data.city_name + ', ' + data.data.temp + 'ºC' + ' ' + data.data.description
    //             document.getElementsByClassName('temperature')[0].innerText = temp;
    //         })
    // }

    // useEffect(() => {
    //     reloadTemperature()
    //     setInterval(reloadTemperature, 1000000);
    // }, [])

    return (
        <>
            <IconContext.Provider value={{color: '#fff'}}>
                <div className='navbar'>
                    <Link className='menu-bars'>
                        <FaIcons.FaBars onClick={showSidebar}/>
                    </Link>
                </div>
                <nav className={sidebar ? 'nav-menu active' : 'nav-menu'}>
                    <ul className='nav-menu-itens' onClick={showSidebar}>
                        <li className='navbar-toogle'>
                            <Link className='menu-bars'>
                                <AiIcons.AiOutlineClose />
                            </Link>
                        </li>
                        <li className='temperature'></li>
                        {parameters.permission.map((value, index) => {
                            return (
                                <li key={index} className={SidebarData[value].menu.cName}>
                                    <Link to={SidebarData[value].menu.path}>
                                        {SidebarData[value].menu.icon}
                                        <span>{SidebarData[value].menu.title}</span>
                                    </Link>
                                </li>
                            )
                        })}
                    </ul>
                </nav>
                
            </IconContext.Provider>
        </>
    )
}

export default NavBar