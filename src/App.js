import React from 'react';
import { GoogleOAuthProvider } from '@react-oauth/google';
import FrontendApp from './FrontendApp';

const CLIENT_ID = '474362067828-c079sdjk79tj2lr6pejegt97kaoekqfg.apps.googleusercontent.com';

function App() {
  return (
    <GoogleOAuthProvider clientId={CLIENT_ID}>
      <FrontendApp />
    </GoogleOAuthProvider>
  );
}

export default App;
