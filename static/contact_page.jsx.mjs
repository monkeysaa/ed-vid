import React from 'react'; 
import ReactDOM, { render } from 'react-dom';


class User extends React.Component {
  constructor(props) {
    super(props);
    this.super = {
      password: 'test',
      authorized: true
    };
    this.authorize = this.authorize.bind(this);
  }
}

authorize(event) {
// if correct password, authorize. 
}

render() {
  const login = (
    <form>
      {/* Make accessible */}
      <input type="password"></input> 
      <button type="submit">Submit</button>
    </form>
  );

  const contactInfo = (
    <ul>
      <li>
        sample_user_name
      </li>
      <li>
        example@email.com
      </li>
    </ul>
  )
  
  return (
    <div> 
      <h1>{ this.StaticRange.authorized ? 'Contact' : 'Enter the Password' } </h1>
      <p> { this.state.authorized ? contactInfo : '' } </p>
    </div>
  )
}

ReactDOM.render(
  <Contact />, 
  document.getElementById('app')
);