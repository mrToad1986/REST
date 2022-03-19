import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import Menu from './components/Menu.js';
import Footer from './components/Footer.js';
import UserList from './components/UserList.js';
import ProjectList from "./components/ProjectList.js";
import TODOlist from "./components/TODOlist.js";
import UserProjectList from "./components/UserProjectList.js"
import {HashRouter, BrowserRouter, Route, Routes, Link, useLocation} from "react-router-dom";

const NotFound = () => {
    let location = useLocation()
    return(
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
        'TODOs': []
    }
  }

  componentDidMount() {
      axios
          .get('http://127.0.0.1:8000/api/users/')
          .then(responce =>{
              const users = responce.data
              this.setState({
                  'users': users
              })
          })
          .catch(error => console.log(error))
      axios
          .get('http://127.0.0.1:8000/api/project/')
          .then(responce =>{
              const projects = responce.data
              this.setState({
                  'projects': projects
              })
          })
          .catch(error => console.log(error))
      axios
          .get('http://127.0.0.1:8000/api/todo/')
          .then(responce =>{
              const TODOs = responce.data
              this.setState({
                  'TODOs': TODOs
              })
          })
          .catch(error => console.log(error))

  }

    render(){
    return(
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
                </nav>
                <Routes>
                    <Route exact path='/users' element={<UserList users={this.state.users}/>}/>
                    <Route exact path='/project' element={<ProjectList projects={this.state.projects}/>}/>
                    <Route exact path='/todo' element={<TODOlist TODOs={this.state.TODOs}/>}/>
                    <Route path ='/user/:id' element={<UserProjectList projects={this.state.books}/>}/>
                    <Route path='*' element={<NotFound/>}/>
                </Routes>
            </BrowserRouter>
            <Footer/>
        </div>
    )
  }
}
export default App;