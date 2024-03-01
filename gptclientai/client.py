class Chat:
    @staticmethod
    def create_chat_response(
            provider,
            messages: list,
            stream: bool = False
    ):
        """
        Return a string or an iteration for the chat completion.

        Args:
            - provider => Exemple : gptclientai.Provider.FreeChatGpt ( Provider to use )
            - messages => Exemple : [{"role": "user", "content": "hello"}] ( Messages of the conversation in a list )
            - stream   => Exemple : True / False ( return a string or an iteration )
        """
        result = provider.create_response(messages)
        return result if stream else "".join([str(chunk) for chunk in result])

class Completion:
    @staticmethod
    def create_completion(
            provider,
            prompt: str,
            stream: bool = False
    ):
        """
        Return a string or an iteration for the completion.

        Args:
            - provider => Exemple : gptclientai.Provider.FreeChatGpt ( Provider to use )
            - prompt   => Exemple : "Hello !" ( Message for the response )
            - stream   => Exemple : True / False ( return a string or an iteration )
        """
        result = provider.create_response([{"role": "user", "content": prompt}])
        return result if stream else "".join([str(chunk) for chunk in result])