import React from 'react'
import * as BsIcons from 'react-icons/bs'
import * as AiIcons from 'react-icons/ai'
import * as GiIcons from 'react-icons/gi'
import * as IoIcons from 'react-icons/io'

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
        icon: <GiIcons.GiBookmark />,
        cName: 'nav-text'
    },
    {
        title: 'Cadastro Série',
        path: '/cadastro-serie',
        icon: <IoIcons.IoMdSchool />,
        cName: 'nav-text'
    },
    {
        title: 'Cadastro Período',
        path: '/cadastro-periodo-academico',
        icon: <BsIcons.BsFillCalendarFill />,
        cName: 'nav-text'
    },
    {
        title: 'Cadastro Nota',
        path: '/cadastro-nota',
        icon: <BsIcons.BsFileEarmarkText />,
        cName: 'nav-text'
    },
    {
        title: 'Cadastro Tipo de nota',
        path: '/cadastro-tipo-nota',
        icon: <IoIcons.IoMdOptions />,
        cName: 'nav-text'
    }
    
]