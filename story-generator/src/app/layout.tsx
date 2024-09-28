import React from 'react';
import './globals.css'; // Import global styles

export const metadata = {
  title: 'Story Generator',
  description: 'Generate escape room stories dynamically',
};

const RootLayout = ({ children }: { children: React.ReactNode }) => (
  <html lang="en">
    <body>
      <main className="container mx-auto p-4">
        {children}
      </main>
    </body>
  </html>
);

export default RootLayout;
