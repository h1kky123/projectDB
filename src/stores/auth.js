// src/stores/auth.js
import { ref } from 'vue';

export const isAuthenticated = ref(localStorage.getItem('isAuthenticated') === 'true');
export const userRole = ref(localStorage.getItem('userRole') || 'user');
export const token = ref(localStorage.getItem('token') || '');

export async function login(email, password) {
  const response = await fetch('/api/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  });
  const data = await response.json();
  if (response.ok) {
    isAuthenticated.value = true;
    userRole.value = data.role;
    token.value = data.token;
    localStorage.setItem('isAuthenticated', 'true');
    localStorage.setItem('userRole', data.role);
    localStorage.setItem('token', data.token);
    return data;
  }
  throw new Error(data.error);
}

export function logout() {
  isAuthenticated.value = false;
  userRole.value = 'user';
  token.value = '';
  localStorage.removeItem('isAuthenticated');
  localStorage.removeItem('userRole');
  localStorage.removeItem('token');
}