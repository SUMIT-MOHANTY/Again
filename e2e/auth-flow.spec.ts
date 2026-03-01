import { test, expect } from '@playwright/test';

test.describe('Authentication Flow', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
  });

  test('successful registration', async ({ page }) => {
    const timestamp = Date.now();
    await page.fill('input[name="email"]', `newuser${timestamp}@example.com`);
    await page.fill('input[name="password"]', 'password123');
    await page.fill('input[name="fullName"]', 'Test User');
    await page.click('button[type="submit"]');
    
    await page.waitForURL('/');
    await expect(page.locator('text=Test User')).toBeVisible();
  });

  test('successful login', async ({ page }) => {
    await page.fill('input[name="email"]', 'test@example.com');
    await page.fill('input[name="password"]', 'password123');
    await page.click('button[type="submit"]');
    
    await page.waitForURL('/');
    await expect(page.locator('text=Dashboard')).toBeVisible();
  });

  test('login with invalid credentials', async ({ page }) => {
    await page.fill('input[name="email"]', 'test@example.com');
    await page.fill('input[name="password"]', 'wrongpassword');
    await page.click('button[type="submit"]');
    
    await expect(page.locator('text=Invalid credentials')).toBeVisible();
  });

  test('logout flow', async ({ page }) => {
    await page.fill('input[name="email"]', 'test@example.com');
    await page.fill('input[name="password"]', 'password123');
    await page.click('button[type="submit"]');
    
    await page.waitForURL('/');
    await page.click('text=Logout');
    
    await expect(page.locator('text=Login')).toBeVisible();
  });

  test('unauthorized access to protected route', async ({ page }) => {
    await page.goto('/portfolio');
    await page.waitForURL('/login');
    await expect(page.locator('text=Please log in')).toBeVisible();
  });

  test('password validation', async ({ page }) => {
    await page.goto('/register');
    await page.fill('input[name="email"]', 'test@example.com');
    await page.fill('input[name="password"]', 'short');
    await page.fill('input[name="fullName"]', 'Test');
    await page.click('button[type="submit"]');
    
    await expect(page.locator('text=Password must be at least')).toBeVisible();
  });
});
