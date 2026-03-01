import { test, expect } from '@playwright/test';

test.describe('Portfolio Management', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
    await page.fill('input[name="email"]', 'test@example.com');
    await page.fill('input[name="password"]', 'password123');
    await page.click('button[type="submit"]');
    await page.waitForURL('/');
  });

  test('create new portfolio', async ({ page }) => {
    await page.click('text=Create Portfolio');
    await page.fill('input[name="title"]', 'My New Portfolio');
    await page.fill('textarea[name="description"]', 'This is my portfolio description');
    
    await page.click('button:has-text("Save")');
    
    await expect(page.locator('text=My New Portfolio')).toBeVisible();
    await expect(page.locator('text=This is my portfolio description')).toBeVisible();
  });

  test('view portfolio details', async ({ page }) => {
    await page.goto('/portfolio/1');
    await expect(page.locator('h1')).toBeVisible();
  });

  test('edit portfolio', async ({ page }) => {
    await page.goto('/portfolio/1');
    await page.click('text=Edit');
    
    await page.fill('input[name="title"]', 'Updated Portfolio Title');
    await page.click('button:has-text("Update")');
    
    await expect(page.locator('text=Updated Portfolio Title')).toBeVisible();
  });

  test('delete portfolio', async ({ page }) => {
    await page.goto('/portfolio');
    const initialCount = await page.locator('.portfolio-card').count();
    
    await page.locator('.portfolio-card').first().hover();
    await page.click('text=Delete');
    await page.click('button:has-text("Confirm")');
    
    await expect(page.locator('.portfolio-card')).toHaveCount(initialCount - 1);
  });

  test('add project to portfolio', async ({ page }) => {
    await page.goto('/portfolio/1');
    await page.click('text=Add Project');
    
    await page.fill('input[name="name"]', 'New Project');
    await page.fill('textarea[name="description"]', 'Project description');
    await page.fill('input[name="url"]', 'https://example.com');
    await page.fill('input[name="technologies"]', 'React, TypeScript');
    
    await page.click('button:has-text("Save Project")');
    
    await expect(page.locator('text=New Project')).toBeVisible();
  });

  test('add skill to portfolio', async ({ page }) => {
    await page.goto('/portfolio/1');
    await page.click('text=Add Skill');
    
    await page.fill('input[name="name"]', 'Python');
    await page.selectOption('select[name="level"]', '5');
    
    await page.click('button:has-text("Save Skill")');
    
    await expect(page.locator('text=Python')).toBeVisible();
  });

  test('search portfolios', async ({ page }) => {
    await page.fill('input[name="search"]', 'python');
    await page.click('button:has-text("Search")');
    
    await expect(page.locator('.portfolio-card').first()).toBeVisible();
  });

  test('validation - empty title', async ({ page }) => {
    await page.click('text=Create Portfolio');
    await page.fill('input[name="title"]', '');
    await page.click('button:has-text("Save")');
    
    await expect(page.locator('text=Title is required')).toBeVisible();
  });

  test('validation - invalid URL', async ({ page }) => {
    await page.goto('/portfolio/1');
    await page.click('text=Add Project');
    
    await page.fill('input[name="name"]', 'Test Project');
    await page.fill('input[name="url"]', 'not-a-url');
    await page.click('button:has-text("Save Project")');
    
    await expect(page.locator('text=Invalid URL')).toBeVisible();
  });
});
