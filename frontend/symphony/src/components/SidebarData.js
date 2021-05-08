import React from 'react'
import * as BsIcons from 'react-icons/bs'
import * as AiIcons from 'react-icons/ai'
import * as GiIcons from 'react-icons/gi'
import * as IoIcons from 'react-icons/io'
import * as BiIcons from 'react-icons/bi'
import * as VscIcons from 'react-icons/vsc'
import * as MdIcons from 'react-icons/md'

import Home from '../pages/home'
import CadastroPessoa from '../pages/cadastro-pessoa'
import CadastroSerie from '../pages/cadastro-serie'
import CadastroPeriodo from '../pages/cadastro-periodo-academico'
import CadastroDisciplina from '../pages/cadastro-disciplina'
import CadastroNota from '../pages/cadastro-nota'
import CadastroTipoNota from '../pages/cadastro-tipo-nota'
import CadastroHorario from '../pages/cadastro-horario'
import CadastroModulo from '../pages/cadastro-modulo'
import ListaErros from '../pages/lista-erros'
import ListaAuditoria from '../pages/lista-auditoria'

import PrivateRout from './PrivateRout'

export const SidebarData = {
    'Home': {
        title: 'Home',
        path: '/',
        icon: <AiIcons.AiFillHome />,
        cName: 'nav-text',
        route: <PrivateRout component={Home} path="/" exact/>
    },
    'Cadastro Pessoa': {
        title: 'Cadastro Pessoa',
        path: '/cadastro-pessoa',
        icon: <BsIcons.BsFillPersonLinesFill />,
        cName: 'nav-text',
        route: <PrivateRout component={CadastroPessoa} path="/cadastro-pessoa"/>
    },
    'Cadastro Disciplina': {
        title: 'Cadastro Disciplina',
        path: '/cadastro-disciplina',
        icon: <GiIcons.GiBookmark />,
        cName: 'nav-text',
        route: <PrivateRout component={CadastroDisciplina} path="/cadastro-disciplina"/>
    },
    'Cadastro Série': {
        title: 'Cadastro Série',
        path: '/cadastro-serie',
        icon: <IoIcons.IoMdSchool />,
        cName: 'nav-text',
        route: <PrivateRout component={CadastroSerie} path="/cadastro-serie"/>
    },
    'Cadastro Período': {
        title: 'Cadastro Período',
        path: '/cadastro-periodo-academico',
        icon: <BsIcons.BsFillCalendarFill />,
        cName: 'nav-text',
        route: <PrivateRout component={CadastroPeriodo} path="/cadastro-periodo-academico"/>
    },
    'Cadastro Nota': {
        title: 'Cadastro Nota',
        path: '/cadastro-nota',
        icon: <BsIcons.BsFileEarmarkText />,
        cName: 'nav-text',
        route: <PrivateRout component={CadastroNota} path="/cadastro-nota"/>
    },
    'Cadastro Tipo de Nota': {
        title: 'Cadastro Tipo de Nota',
        path: '/cadastro-tipo-nota',
        icon: <IoIcons.IoMdOptions />,
        cName: 'nav-text',
        route: <PrivateRout component={CadastroTipoNota} path="/cadastro-tipo-nota"/>
    },
    'Cadastro Horário': {
        title: 'Cadastro Horário',
        path: '/cadastro-horario',
        icon: <BiIcons.BiTime />,
        cName: 'nav-text',
        route: <PrivateRout component={CadastroHorario} path="/cadastro-horario"/>
    },
    'Cadastro Módulo': {
        title: 'Cadastro Módulo',
        path: '/cadastro-modulo',
        icon: <BiIcons.BiTime />,
        cName: 'nav-text',
        route: <PrivateRout component={CadastroModulo} path="/cadastro-modulo"/>
    },
    'Erros': {
        title: 'Erros',
        path: '/lista-erros',
        icon: <VscIcons.VscError />,
        cName: 'nav-text',
        route: <PrivateRout component={ListaErros} path="/lista-erros"/>
    },
    'Auditoria': {
        title: 'Auditoria',
        path: '/lista-auditoria',
        icon: <MdIcons.MdSystemUpdateAlt />,
        cName: 'nav-text',
        route: <PrivateRout component={ListaAuditoria} path="/lista-auditoria"/>
    }
}
