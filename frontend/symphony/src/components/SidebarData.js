import React from 'react'
import * as BsIcons from 'react-icons/bs'
import * as AiIcons from 'react-icons/ai'

export const SidebarData = [
    {
        title: 'Home',
        path: '/',
        icon: <AiIcons.AiFillHome />,
        cName: 'nav-text'
    },
    {
        title: 'Cadastro Pessoa',
        path: '/cadastro-pessoa',
        icon: <BsIcons.BsFillPersonLinesFill />,
        cName: 'nav-text'
    },
    {
        title: 'Cadastro Disciplina',
        path: '/cadastro-disciplina',
        icon: <AiIcons.AiFillHome />,
        cName: 'nav-text'
    },
    {
        title: 'Cadastro Série',
        path: '/cadastro-serie',
        icon: <BsIcons.BsFillPersonLinesFill />,
        cName: 'nav-text'
    },
    {
        title: 'Cadastro Período',
        path: '/cadastro-periodo-academico',
        icon: <BsIcons.BsFillPersonLinesFill />,
        cName: 'nav-text'
    }
    
]