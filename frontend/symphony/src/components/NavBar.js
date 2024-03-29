import React, {useState} from 'react'
import * as FaIcons from 'react-icons/fa'
import * as AiIcons from 'react-icons/ai'
import { Link } from 'react-router-dom'
import { IconContext } from 'react-icons'

import { SidebarData } from './SidebarData.js'

import '../styles/scss/navbar/navbar.scss'

function NavBar(parameters) {
    const [sidebar, setSidebar] = useState(false)

    const showSidebar = () => setSidebar(!sidebar)
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
                    {parameters.permission.map((value,index) => {
                        return (
                            <li key={index} className={SidebarData[value].cName}>
                                <Link to={SidebarData[value].path}>
                                    {SidebarData[value].icon}
                                    <span>{SidebarData[value].title}</span>
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