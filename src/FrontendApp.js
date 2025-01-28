import React, { useState } from 'react';
import { Card, CardContent } from './components/ui/card';
import { Button } from './components/ui/button';
import { Input } from './components/ui/input';
import { Label } from './components/ui/label';
import { GoogleLogin } from '@react-oauth/google';
import { motion } from 'framer-motion';

const FrontendApp = () => {
  const [step, setStep] = useState(1);
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const handleGoogleLoginSuccess = (credentialResponse) => {
    console.log('Google Login Success:', credentialResponse);
    alert('Google Login Successful!');
  };

  const handleGoogleLoginError = () => {
    console.error('Google Login Failed');
    alert('Google Login Failed');
  };
  const [sourceFile, setSourceFile] = useState(null);
  const [targetFile, setTargetFile] = useState(null);

  const handleNextStep = () => setStep(step + 1);
  const handlePreviousStep = () => setStep(step - 1);

  const handleFileUpload = async () => {
    if (!sourceFile || !targetFile) {
      alert('Please upload both source and target files.');
      return;
    }

    const formData = new FormData();
    formData.append('sourceFile', sourceFile);
    formData.append('targetFile', targetFile);

    try {
      const response = await fetch('/api/upload', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        alert('Files uploaded successfully!');
      } else {
        alert('Failed to upload files.');
      }
    } catch (error) {
      console.error('Error uploading files:', error);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <Card className="w-full max-w-lg p-6">
        <CardContent>
          {step === 1 && (
            <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
              <Label>Name</Label>
              <Input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Enter your name"
              />
              <Label>Email</Label>
              <Input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Enter your email"
              />
              <Button className="mt-4 w-full" onClick={handleNextStep}>
                Next
              </Button>
            </motion.div>
          )}

          {step === 2 && (
            <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
              <h2 className="text-lg font-bold">Google Authenticator</h2>
              <GoogleLogin
                onSuccess={handleGoogleLoginSuccess}
                onError={handleGoogleLoginError}
              />
              <div className="mt-4 flex justify-between">
                <Button onClick={handleNextStep}>Verify</Button>
                <Button onClick={handlePreviousStep}>Back</Button>
              </div>
            </motion.div> 
          )}

          {step === 3 && (
            <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
              <Label>Source File</Label>
              <Input
                type="file"
                onChange={(e) => setSourceFile(e.target.files[0])}
                className="mb-4"
              />
              <Label>Target File</Label>
              <Input
                type="file"
                onChange={(e) => setTargetFile(e.target.files[0])}
                className="mb-4"
              />
              <div className="mt-4 flex justify-between">
                <Button onClick={handlePreviousStep}>Back</Button>
                <Button onClick={handleFileUpload}>Upload</Button>
              </div>
            </motion.div>
          )}
        </CardContent>
      </Card>
    </div>
  );
};

export default FrontendApp;
