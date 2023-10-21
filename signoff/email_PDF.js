{/*doesn't work right now*/}
import React from 'react';

function EmailPDF() {
  const email = '1606mthomas@gmail.com';
  const subject = 'Sending PDF';
  const body = 'Please find the attached PDF.';
  const attachmentURL = 'Document14.pdf';

  const mailtoLink = `mailto:${email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}&attachment=${attachmentURL}`;

  return (
    <a href={mailtoLink}>Send Email with PDF</a>
  );
}

export default EmailPDF;
