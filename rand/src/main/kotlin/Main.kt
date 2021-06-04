import com.londogard.nlp.embeddings.BpeEmbeddings
import com.londogard.nlp.embeddings.EmbeddingLoader
import com.londogard.nlp.embeddings.sentence.USifSentenceEmbeddings
import com.londogard.nlp.tokenizer.SentencePieceTokenizer
import com.londogard.nlp.utils.LanguageSupport
import com.londogard.nlp.utils.cosineDistance
import com.londogard.nlp.wordfreq.WordFrequencies
import java.io.File
import kotlin.system.exitProcess

object Main {
    @JvmStatic
    fun main(args: Array<String>) {
        val allAssignments = File(javaClass.getResource("data/assignment")!!.toURI()).listFiles()
            .flatMap { it.listFiles().toList() }
            .map { it.readText() }

        val allResumes = File(javaClass.getResource("data/resumes")!!.toURI()).listFiles()
            .map { it.readText() }

        println(allAssignments[0])
        println("====")
        println(allResumes[985])
        exitProcess(0)

        val embs = EmbeddingLoader.fromLanguageOrNull<BpeEmbeddings>(LanguageSupport.en)!!
        val sentenceEmbeddings = USifSentenceEmbeddings(embs, WordFrequencies.getAllWordFrequenciesOrNull(LanguageSupport.en)!!)
        val allAss = allAssignments.take(1).map { sentenceEmbeddings.getSentenceEmbedding(it.split(" ")) }
        val tokenizer = SentencePieceTokenizer.fromLanguageSupportOrNull(LanguageSupport.en)!!
        val allRes = allResumes
            .map { tokenizer.split(it) }
            .filter { it.size > 10 }
            .map { sentenceEmbeddings.getSentenceEmbedding(it) }

        print(allRes.withIndex().minByOrNull { it.value.cosineDistance(allAss.first()) }!!.index)
    }
}