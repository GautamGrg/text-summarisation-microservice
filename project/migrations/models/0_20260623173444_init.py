from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "textsummary" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "url" TEXT NOT NULL,
    "summary" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztll1vmzAUhv8K4qqVuqpl6Yd2x9JszdSSqWFb1apCDjgExdjUNmuiKv99PgbCRwjKpE"
    "lrpN7Be17jcx7MObyaMQswEccuXshxGseIL81PxqtJUYzVRVv4yDBRkpRBECSaEO2Xyigq"
    "xomQHPlShaaICKykAAufR4mMGFUqTQkBkfnKGNGwlFIaPafYkyzEcoa5Cjw+KTmiAV5gUd"
    "wmc28aYRLUko4C2FvrnlwmWhtS+UUbYbeJ5zOSxrQ0J0s5Y3TtjqgENcQUcyQxPF7yFNKH"
    "7PJii4qyTEtLlmJlTYCnKCWyUu6ODHxGgZ/KRugCQ9jlg3Xau+hdfjzvXSqLzmStXKyy8s"
    "ras4WagOOaKx1HEmUOjbHklnKyCQ5efTu53N5ApxJuoitAdbErhBJeeWD+Db0ONO7g3oWk"
    "YyGeCQjOT/uuf23fHdza94c6sswjNyPna2Fn6mhnx97p34w+a7olzcpnsCvRypJ3qu1UfY"
    "6hfg/JTbBXKiKjGLfDra9s8A3ypcfFxdukbaoaghEly7y5dNEf3g7Grn37vfYKrmx3ABGr"
    "hr9QD84P629g/RDj19C9NuDWeBg5A02QCRlyvWPpcx9MyAmlknmUvXgoqPTBQi3ArKCDT+"
    "eVXgTCBPnzF8QDbyPCLLbNuxmKrbipIIpC/VoALqSZTzcb88iftc29PNI58lDpeZ92ezTt"
    "fmMuIKUNeP0Z4u30Kkv2pT+rU7/wCKahhANunZ11MCvas3I1+kDRua0sVm/J8Gn8BcTcvp"
    "8AT09OdgCoXFsB6lhjpjEqMW0ZaN/GI2fLMCuXNED+oKrAxyDy5ZFBIiGf3ibWDopQdfd/"
    "Q/MXoTGN4AHw3/Bfx8vqD3DIQmo="
)
