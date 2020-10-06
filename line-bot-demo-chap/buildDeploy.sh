lineKey=$(cat ../.line)
sam build --profile villaaws &&\
sam deploy --profile villaaws --parameter-overrides LineKey=$lineKey
