import React from 'react'
import * as BsIcons from 'react-icons/bs'
import * as AiIcons from 'react-icons/ai'
import * as GiIcons from 'react-icons/gi'
import * as IoIcons from 'react-icons/io'
import * as BiIcons from 'react-icons/bi'
import * as VscIcons from 'react-icons/vsc'
import * as MdIcons from 'react-icons/md'

import Home from '../pages/home'

// cadastros
import CadastroPessoa from '../pages/cadastro-pessoa'
import CadastroGrupoPessoa from '../pages/cadastro-grupo-pessoa'
import CadastroGrupo from '../pages/cadastro-grupo'
import CadastroSerie from '../pages/cadastro-serie'
import CadastroPeriodo from '../pages/cadastro-periodo'
import CadastroDisciplina from '../pages/cadastro-disciplina'
import CadastroNota from '../pages/cadastro-nota'
import CadastroTipoNota from '../pages/cadastro-tipo-nota'
import CadastroHorario from '../pages/cadastro-horario'
import CadastroModulo from '../pages/cadastro-modulo'
import CadastroTurma from '../pages/cadastro-turma'
import CadastroMatriz from '../pages/cadastro-matriz'
import CadastroMatricula from '../pages/cadastro-matricula'
import CadastroTurmaOcorrencia from '../pages/cadastro-turma-ocorrencia'
import CadastroTurmaHorario from '../pages/cadastro-turma-horario'
import CadastroTurmaProfessor from '../pages/cadastro-turma-professor'

// listas
import ListaErros from '../pages/lista-erros'
import ListaAuditoria from '../pages/lista-auditoria'
import ListaPessoa from '../pages/lista-pessoa'
import ListaGrupo from '../pages/lista-grupo'
import ListaHorario from '../pages/lista-horario'
import ListaModulo from '../pages/lista-modulo'
import ListaPeriodo from '../pages/lista-periodo'
import ListaTipoNota from '../pages/lista-tipo-nota'
import ListaSerie from '../pages/lista-serie'
import ListaTurma from '../pages/lista-turma'
import ListaDisciplina from '../pages/lista-disciplina'

import PrivateRout from './PrivateRout'

export const SidebarData = {
    'Home': {
        menu: {
            title: 'Home',
            path: '/',
            icon: <AiIcons.AiFillHome />,
            cName: 'nav-text',
        },
        routes: [
            <PrivateRout component={Home} path="/" exact />
        ]
    },
    'Cadastro Pessoa': {
        menu: {
            title: 'Pessoa',
            path: '/pessoa-list',
            icon: <BsIcons.BsFillPersonLinesFill />,
            cName: 'nav-text',
        },
        routes: [
            <PrivateRout component={ListaPessoa} path="/pessoa-list" />,
            <PrivateRout component={CadastroPessoa} path="/cadastro-pessoa" />,
            <PrivateRout component={CadastroGrupoPessoa} path="/cadastro-grupo-pessoa" />
        ]
    },
    'Cadastro Disciplina': {
        menu: {
            title: 'Disciplina',
            path: '/lista-disciplina',
            icon: <GiIcons.GiBookmark />,
            cName: 'nav-text',
        },
        routes: [
            <PrivateRout component={ListaDisciplina} path="/lista-disciplina" />,
            <PrivateRout component={CadastroDisciplina} path="/cadastro-disciplina" />
        ]
    },
    'Cadastro Série': {
        menu: {
            title: 'Série',
            path: '/lista-serie',
            icon: <IoIcons.IoMdSchool />,
            cName: 'nav-text',
        },
        routes: [
            <PrivateRout component={ListaSerie} path="/lista-serie" />,
            <PrivateRout component={CadastroSerie} path="/cadastro-serie" />,
            <PrivateRout component={CadastroMatriz} path="/cadastro-matriz" />
        ]
    },
    'Cadastro Período': {
        menu: {
            title: 'Período',
            path: '/lista-periodo',
            icon: <BsIcons.BsFillCalendarFill />,
            cName: 'nav-text',
        },
        routes: [
            <PrivateRout component={ListaPeriodo} path="/lista-periodo" />,
            <PrivateRout component={CadastroPeriodo} path="/cadastro-periodo" />
        ]
    },
    'Cadastro Nota': {
        menu: {
            title: 'Cadastro Nota',
            path: '/cadastro-nota',
            icon: <BsIcons.BsFileEarmarkText />,
            cName: 'nav-text',
        },
        routes: [
            <PrivateRout component={CadastroNota} path="/cadastro-nota" />
        ]
    },
    'Cadastro Tipo de Nota': {
        menu: {
            title: 'Tipo de Nota',
            path: '/lista-tipo-nota',
            icon: <IoIcons.IoMdOptions />,
            cName: 'nav-text',
        },
        routes: [
            <PrivateRout component={ListaTipoNota} path="/lista-tipo-nota" />,
            <PrivateRout component={CadastroTipoNota} path="/cadastro-tipo-nota" />
        ]
    },
    'Cadastro Turma': {
        menu: {
            title: 'Turma',
            path: '/lista-turma',
            icon: <IoIcons.IoMdOptions />,
            cName: 'nav-text',
        },
        routes: [
            <PrivateRout component={ListaTurma} path="/lista-turma" />,
            <PrivateRout component={CadastroTurma} path="/cadastro-turma" />,
            <PrivateRout component={CadastroMatricula} path="/cadastro-matricula" />,
            <PrivateRout component={CadastroTurmaOcorrencia} path="/cadastro-turma-ocorrencia" />,
            <PrivateRout component={CadastroTurmaProfessor} path="/cadastro-turma-professor" />,
            <PrivateRout component={CadastroTurmaHorario} path="/cadastro-turma-horario" />

        ]
    },
    'Cadastro Horário': {
        menu: {
            title: 'Horário',
            path: '/lista-horario',
            icon: <BiIcons.BiTime />,
            cName: 'nav-text',
        },
        routes: [
            <PrivateRout component={ListaHorario} path="/lista-horario" />,
            <PrivateRout component={CadastroHorario} path="/cadastro-horario" />
        ]
    },
    'Cadastro Módulo': {
        menu: {
            title: 'Módulo',
            path: '/lista-modulo',
            icon: <BiIcons.BiTime />,
            cName: 'nav-text',
        },
        routes: [
            <PrivateRout component={ListaModulo} path="/lista-modulo" />,
            <PrivateRout component={CadastroModulo} path="/cadastro-modulo" />
        ]
    },
    'Cadastro Grupo': {
        menu: {
            title: 'Grupo',
            path: '/lista-grupo',
            icon: <BiIcons.BiTime />,
            cName: 'nav-text',
        },
        routes: [
            <PrivateRout component={ListaGrupo} path="/lista-grupo" />,
            <PrivateRout component={CadastroGrupo} path="/cadastro-grupo" />
        ]
    },
    'Erros': {
        menu: {
            title: 'Erros',
            path: '/lista-erros',
            icon: <VscIcons.VscError />,
            cName: 'nav-text',
        },
        routes: [
            <PrivateRout component={ListaErros} path="/lista-erros" />
        ]
    },
    'Auditoria': {
        menu: {
            title: 'Auditoria',
            path: '/lista-auditoria',
            icon: <MdIcons.MdSystemUpdateAlt />,
            cName: 'nav-text',
        },
        routes: [
            <PrivateRout component={ListaAuditoria} path="/lista-auditoria" />
        ]
    }
}
