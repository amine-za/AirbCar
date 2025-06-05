# Airbcar Month 1 To-Do List: Core Infrastructure Setup

**Date**: June 2025

**Objective**: Establish the foundation for Airbcar with authentication, PostgreSQL database, user APIs, frontend landing page, DevOps infrastructure, and UI/UX designs to launch Morocco’s top car rental platform.

**Team**:
- **Naoufal Chaknan**: Frontend Developer
- **Amine Zaghloul**: Backend Developer
- **Mohamed Yassine Ayache**: FullStack Support, UI/UX, DevOps

**Motivation**: We’re building the core of a revolutionary rental platform! Let’s lay a rock-solid foundation together! 🚗🚀

## Amine Zaghloul (Backend Developer)

- [ ] Install and configure Django with PostgreSQL connector (`psycopg2-binary`).
- [ ] Create PostgreSQL database (`airbcar_db`) and user (`airbcar_user`).
- [ ] Set up JWT authentication for login, sign-up, and password reset flows.
- [ ] Update project settings to use PostgreSQL and custom user model (`core.User`).
- [ ] Test database connection and authentication endpoints.
- [ ] Finalize PostgreSQL schema for `User` model (fields: `phone_number`, `profile_picture`, `default_currency`, `is_partner`, `is_verified`).
- [ ] Create user management APIs (`/users/`) for CRUD operations.
- [ ] Implement serializers and views for user APIs.
- [ ] Apply migrations for `User` model and verify `core_user` table.
- [ ] Add sample users (e.g., admin, partner, renter) to test APIs.
- **Motivation**: You’re powering the backend engine, Amine—making Airbcar secure and functional! 💪

## Naoufal Chaknan (Frontend Developer)

- [ ] Set up Next.js project with basic folder structure.
- [ ] Create responsive landing page for customers (search bar, basic filters).
- [ ] Build login, sign-up, and password reset pages with responsive design.
- [ ] Implement form validation for login and sign-up inputs.
- [ ] Integrate auth pages with backend JWT authentication APIs.
- [ ] Test landing page responsiveness on mobile, tablet, and desktop.
- [ ] Add language switcher (Arabic, French, English) to landing page.
- **Motivation**: Your UI is Airbcar’s first impression, Naoufal—make it unforgettable! 🌟

## Mohamed Yassine Ayache (FullStack/UI/UX/DevOps)

- [ ] Initialize GitHub repository with branch protection rules.
- [ ] Configure Docker for PostgreSQL and Redis caching.
- [ ] Set up AWS S3 bucket for file storage (e.g., profile pictures).
- [ ] Create Figma wireframes for landing page, auth pages, and dashboard layouts.
- [ ] Set up GitHub Actions for basic CI/CD pipeline (linting, tests).
- [ ] Configure Postman collection for testing backend APIs.
- [ ] Assist with PostgreSQL setup and user API integration.
- [ ] Review Figma designs with team for feedback.
- **Motivation**: You’re the mastermind tying it all together, Yassine—building a seamless system! 🛠️

## Notes

- **Blockers**: Log issues (e.g., PostgreSQL errors, API integration) in this file for team review.

---