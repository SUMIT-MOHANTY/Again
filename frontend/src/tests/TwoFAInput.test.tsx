import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { Provider } from 'react-redux';
import configureStore from 'redux-mock-store';
import TwoFAInput from '../components/TwoFAInput';
import * as api from '../services/apiClient';

const mockStore = configureStore([]);
jest.mock('../services/apiClient');

describe('TwoFAInput', () => {
  it('submits code and handles success', async () => {
    (api.apiClient.post as jest.Mock).mockResolvedValueOnce({ success: true });
    const store = mockStore({ auth: { loading: false, twoFAError: null, jwt: 'token', isAuthenticated: false } });
    render(<Provider store={store}><TwoFAInput /></Provider>);
    fireEvent.change(screen.getByLabelText(/2fa code/i), { target: { value: '123456' } });
    fireEvent.click(screen.getByRole('button', { name: /verify/i }));
    await waitFor(() => expect(api.apiClient.post).toHaveBeenCalled());
  });
});
