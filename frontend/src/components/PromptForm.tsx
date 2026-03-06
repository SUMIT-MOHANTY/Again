import React from 'react';
export const PromptForm = () => (
  <form>
    <label htmlFor='prompt'>Prompt</label>
    <input id='prompt' name='prompt' type='text' />
    <button type='submit'>Submit</button>
  </form>
);
