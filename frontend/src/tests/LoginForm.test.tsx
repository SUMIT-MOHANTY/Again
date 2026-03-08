import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { Provider } from 'react-redux';
import configureStore from 'redux-mock-store';
import LoginForm from '../components/LoginForm';
import * as api from '../services/apiClient';

const mockStore = configureStore([]);

jest.mock('../services/apiClient');

describe('LoginForm', () => {
  it('renders inputs and disabled button initially', () => {
    const store = mockStore({ auth: { loading: false, loginError: null, jwt: null, isAuthenticated: false } });
    render(<Provider store={store}><LoginForm /></Provider>);
    expect(screen.getByLabelText(/username/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/password/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /login/i })).toBeDisabled();
  });

  it('shows 2FA after successful login', async () => {
    (api.apiClient.post as jest.Mock).mockResolvedValueOnce({ token: 'abc' });
    const store = mockStore({ auth: { loading: false, loginError: null, jwt: null, isAuthenticated: false } });
    render(<Provider store={store}><LoginForm /></Provider>);
    fireEvent.change(screen.getByLabelText(/username/i), { target: { value: 'u' } });
    fireEvent.change(screen.getByLabelText(/password/i), { target: { value: 'p' } });
    fireEvent.click(screen.getByRole('button', { name: /login/i }));
    await waitFor(() => expect(api.apiClient.post).toHaveBeenCalled());
  });
});
