## This is my first logger pratices 

---
## WorKFlow of Logging:


                    ┌──────────────┐
                    │   LOGGER     │
                    │              │
                    │ logger.info()│
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │   HANDLER    │
                    │              │
                    │ FileHandler  │
                    │ StreamHandler│
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  FORMATTER   │
                    │              │
                    │ %(levelname)s│
                    │ %(message)s  │
                    └──────┬───────┘
                           │
                           ▼
                    employee.log
                    OR Terminal

---