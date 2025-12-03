UPDATE "users" SET "password" = 'oops!' WHERE "username" = 'admin';

DELETE FROM "user_logs" WHERE "new_password" = 'oops!';


INSERT INTO "user_logs" ("type","old_username","new_username","old_password","new_password",)

