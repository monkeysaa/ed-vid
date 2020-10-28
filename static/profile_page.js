import React from 'react';
import ReactDOM from 'react-dom';
import { NavBar } from './NavBar.js';

class ProfilePage extends React.Component {
  render(){
    return (
      <main>
        <h1>All About Me!</h1>
        <p>I teach music to kids K-8 and etc</p>
        <img src= '/images/img0.jpg'/>
      </main>
    );
  }
}

ReactDOM.render(
  <ProfilePage/>,
  document.getElementById('app')
);
