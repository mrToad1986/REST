import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import Menu from './components/Menu.js';
import Footer from './components/Footer.js';
import UserList from './components/UserList.js';
import ProjectList from "./components/ProjectList.js";
import TODOlist from "./components/TODOlist.js";
import UserProjectList from "./components/UserProjectList.js";
import LoginForm from "./components/LoginForm.js";
import Cookies from 'universal-cookie';
import {HashRouter, BrowserRouter, Route, Routes, Link, useLocation} from "react-router-dom";

const NotFound = () => {
    let location = useLocation()
    return (
        <div>
            Page {location.pathname} not found
        </div>
    )
}


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'TODOs': [],
            'token': [],
        }
    }

    getData() {
        let headers = this.getHeader()
        axios
            .get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
                const users = response.data
                this.setState({
                    'users': users
                })
            })
            .catch(error => {
                console.log(error)
                this.setState({
                    'users': []
                })
            })
        axios
            .get('http://127.0.0.1:8000/api/project/', {headers})
            .then(response => {
                const projects = response.data
                this.setState({
                    'projects': projects
                })
            })
            .catch(error => {
                console.log(error)
                this.setState({
                    'projects': []
                })
            })
        axios
            .get('http://127.0.0.1:8000/api/todo/', {headers})
            .then(response => {
                const TODOs = response.data
                this.setState({
                    'TODOs': TODOs
                })
            })
            .catch(error => {
                console.log(error)
                this.setState({
                    'TODOs': []
                })
            })
    }

    componentDidMount() {
        let token = localStorage.getItem("token")
        this.setState({
            "token": token
        }, this.getData)
    }

    isAuth() {
        return !!this.state.token
    }

    getHeader() {
        if (this.isAuth()) {
//            console.log(this.state.token)
            return {
                'Authorization': 'Token' + this.state.token
            }
        }
    }

    getToken(login, password) {
        console.log(login, password)
        axios
            .post('http://127.0.0.1:8000/api-auth-token/', {'username': login, 'password': password})
            .then(response => {
                const token = response.data.token
                console.log(token)
                localStorage.setItem("token", token)
                this.setState({
                    'token': token
                }, this.getData)
            })
            .catch(error => console.log(error))
    }

    logout() {
        localStorage.setItem("token", "")
        this.setState({
            'token': ""
        }, this.getData)
    }


    render() {
        return (
            <div>
                <Menu/>
                <BrowserRouter>
                    <nav>
                        <li>
                            <Link to='/users'>Users</Link>
                        </li>
                        <li>
                            <Link to='/project'>Projects</Link>
                        </li>
                        <li>
                            <Link to='/todo'>TODOs</Link>
                        </li>
                        <li>
                            {this.isAuth() ? <button onClick={() => this.logout()}>Logout</button> :
                                <Link to='/login'>Login</Link>}
                        </li>
                    </nav>
                    <Routes>
                        <Route exact path='/users' element={<UserList users={this.state.users}/>}/>
                        <Route exact path='/project' element={<ProjectList projects={this.state.projects}/>}/>
                        <Route exact path='/todo' element={<TODOlist TODOs={this.state.TODOs}/>}/>
                        <Route exact path='/login'
                               element={<LoginForm getToken={(login, password) => this.getToken(login, password)}/>}/>
                        <Route path='/user/:id' element={<UserProjectList users={this.state.users}/>}/>
                        <Route path='*' element={<NotFound/>}/>
                    </Routes>
                </BrowserRouter>
                <Footer/>
            </div>
        )
    }
}

export default App;