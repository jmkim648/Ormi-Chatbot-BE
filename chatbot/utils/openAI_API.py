import openai
from environ import Env
from pathlib import Path
from django.conf import settings
from .prompt_data import prompt_data

env = Env()
env_path: Path = settings.BASE_DIR / '.env'
if env_path.is_file():
    with env_path.open('rt', encoding='utf-8') as f:
        env.read_env(f, overwrite=True)


class OpenAIAPI:
    openai.api_key = env.str("OPENAI_API_KEY")

    @staticmethod
    def generate_response(user_message, lang, convention):
        system_prompts = [
                    {"role": "system", "content": "assistant는 함수명, 변수명 추천 챗봇이다."},
                    {"role": "system", "content": f"assistant는 사무적인 {lang} 전문가다."},
                ]
        if not convention:
            system_prompts.append(
                {"role": "system", "content": f"assistant는 코드를 {lang} 언어의 스타일로 보여준다."}
            )
        else:
            system_prompts.append(
                {"role": "system", "content": f"assistant는 코드를 {lang} 언어의 {convention} 문서에 기반한 스타일로 보여준다."}
            )
        prompt_message = [{"role": "user", "content": user_message}]
        prompt = system_prompts + prompt_data + prompt_message
        prompt_str = str(prompt).replace("'", '"')
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt_str,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.7,
        )

        return response["choices"][0]["text"].split('"content":')[-1].split("created_at")[0].strip()[1:-2]