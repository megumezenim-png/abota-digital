# ABOTA Digital

Primeira fatia demonstrativa de uma aplicação para gestão de grupos de abota. A interface usa dados de exemplo claramente identificados; ainda não regista operações financeiras reais.

## Estrutura

- `frontend/`: React, TypeScript/TSX, Vite, PWA e configuração Capacitor.
- `backend/`: API Python/FastAPI e modelos SQLAlchemy/PostgreSQL.
- `render.yaml`: definição inicial da API e da base PostgreSQL no Render.

## Desenvolvimento frontend

```bash
pnpm install
pnpm dev
```

Para compilar: `pnpm build`. A PWA está preparada com manifesto e service worker; no iPhone, abrir o endereço publicado no Safari e usar Partilhar → Adicionar ao ecrã principal.

Para uma verificação local de produção, execute `pnpm build` e `python3 -m compileall -q backend/app backend/migrations`. O script `scripts/check-production.sh` executa build e migrações, mas exige `DATABASE_URL` válida e acesso à base de dados; não o execute contra produção sem rever o alvo.

## API local

A partir da raiz, crie um ambiente virtual e instale `backend/requirements.txt`. Em seguida execute `uvicorn app.main:app --app-dir backend --reload --port 8000`. A verificação de saúde fica em `/health`; a documentação OpenAPI em `/api/docs`. Defina `DATABASE_URL` e `CORS_ORIGINS` no ambiente, nunca em ficheiros versionados.

## Android

A configuração Capacitor usa o identificador `com.abotadigital.app`. Instale/prepare o Android SDK, execute `pnpm android:sync` e abra o projeto Android gerado com `pnpm android:open`. Assinatura APK e distribuição exigem configuração de keystore e ferramentas Android próprias.

## Render

`render.yaml` prepara um Web Service Python e PostgreSQL. Antes de criar recursos, rever região/plano/custos no Render e definir `CORS_ORIGINS` com a origem da aplicação web. A configuração não contém chaves secretas. A integração persistente PostgreSQL, autenticação e migrações devem ser finalizadas antes de usar dados reais.

No Render, crie um Blueprint a partir deste repositório e reveja os recursos e custos antes de confirmar. A API verifica `/health`; `/health/db` confirma a ligação PostgreSQL e `/api/v1/groups` consulta os grupos persistidos. Configure `CORS_ORIGINS` no serviço com a origem HTTPS final do frontend. O `preDeployCommand` executa `alembic upgrade head`; não há migrações aplicadas enquanto o serviço Render não for criado.

Para Android, `scripts/build-android-apk.sh` compila APK debug quando JDK, `ANDROID_HOME`/`ANDROID_SDK_ROOT`, Android SDK e Gradle Wrapper estiverem disponíveis. Para distribuição, é necessário configurar assinatura release/keystore de forma segura.
