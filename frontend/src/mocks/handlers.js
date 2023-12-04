import { rest } from "msw";

const baseURL = "https://socially-api-6488718a0b5b.herokuapp.com/";

export const handlers = [
  rest.get(`${baseURL}dj-rest-auth/user/`, (req, res, ctx) => {
    return res(
      ctx.json({
        pk: 6,
        username: "test_user4",
        email: "",
        first_name: "",
        last_name: "",
        profile_id: 6,
        profile_image:
          "https://res.cloudinary.com/dowbhp8px/image/upload/v1/media/../default_profile_fhjejn",
      })
    );
  }),
  rest.post(`${baseURL}dj-rest-auth/logout/`, (req, res, ctx) => {
    return res(ctx.status(200));
  }),
];
