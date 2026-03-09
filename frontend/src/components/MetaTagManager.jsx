import React from 'react';
import { Helmet } from 'react-helmet';

export const MetaTagManager = ({ title, description, ogImage, url, canonical }) => (
  <Helmet>
    <title>{title}</title>
    <meta name="description" content={description} />
    {canonical && <link rel="canonical" href={canonical} />}
    <meta property="og:title" content={title} />
    <meta property="og:description" content={description} />
    <meta property="og:image" content={ogImage} />
    <meta property="og:url" content={url} />
    <meta name="twitter:card" content="summary_large_image" />
  </Helmet>
);
