import React, { Component } from 'react';

import './Footer.css';

const Footer = (props) => {
  return (
    <footer>
      <div className="footer container">
        <ul>
          <li><a href="#">coffee recipes</a></li>
          <li><a href="#">subscribe</a></li>
          <li><a href="#">about</a></li>
          <li><a href="#">contact</a></li>
        </ul>
      </div>
      <small>&copy;
        <script type="text/javascript">
          document.write(new Date().getFullYear());
        </script>
        &nbsp;jastr945; Icon made by <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></small>
    </footer>
  )
}

export default Footer;
